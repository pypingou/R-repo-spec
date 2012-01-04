%global packname  catmap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Case-control And Tdt Meta-Analysis Package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
catmap is an R package that conducts fixed-effects (inverse variance) and
random-effects (DerSimonian and Laird, 1986) meta-analyses of case-control
or family-based (TDT) genetic data; in addition, it performs meta-analyses
combining these two types of study designs.  The fixed-effects model was
first described by Kazeem and Farrell (2005); the random-effects model is
described in Nicodemus (submitted).

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/catmap/html
%doc %{rlibdir}/catmap/DESCRIPTION
%{rlibdir}/catmap/INDEX
%{rlibdir}/catmap/help
%{rlibdir}/catmap/Meta
%{rlibdir}/catmap/data
%{rlibdir}/catmap/NAMESPACE
%{rlibdir}/catmap/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6-1
- initial package for Fedora