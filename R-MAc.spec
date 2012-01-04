%global packname  MAc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Meta-Analysis with Correlations

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This is an integrated meta-analysis package for conducting a correlational
research synthesis. One of the unique features of this package is in its
integration of user-friendly functions to facilitate statistical analyses
at each stage in a meta-analysis with correlations. It uses recommended
procedures as described in The Handbook of Research Synthesis and
Meta-Analysis (Cooper, Hedges, & Valentine, 2009).

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
%doc %{rlibdir}/MAc/DESCRIPTION
%doc %{rlibdir}/MAc/doc
%doc %{rlibdir}/MAc/html
%{rlibdir}/MAc/Meta
%{rlibdir}/MAc/NAMESPACE
%{rlibdir}/MAc/INDEX
%{rlibdir}/MAc/R
%{rlibdir}/MAc/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora