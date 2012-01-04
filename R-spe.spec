%global packname  spe
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Stochastic Proximity Embedding

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implements stochastic proximity embedding as described by Agrafiotis et
al. in PNAS, 2002, 99, pg 15869 and J. Comput. Chem., 2003,24, pg 1215

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
%doc %{rlibdir}/spe/html
%doc %{rlibdir}/spe/DESCRIPTION
%{rlibdir}/spe/INDEX
%{rlibdir}/spe/help
%{rlibdir}/spe/data
%{rlibdir}/spe/Meta
%{rlibdir}/spe/libs
%{rlibdir}/spe/R
%{rlibdir}/spe/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora