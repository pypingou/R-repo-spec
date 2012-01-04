%global packname  anapuce
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Tools for microarray data analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains functions for normalisation,differentially analysis
of microarray data and others functions implementing recent methods
developed by the Statistic and Genom Team from UMR 518 AgroParisTech/INRA
Appl. Math. Comput. Sc.

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
%doc %{rlibdir}/anapuce/html
%doc %{rlibdir}/anapuce/DESCRIPTION
%{rlibdir}/anapuce/INDEX
%{rlibdir}/anapuce/NAMESPACE
%{rlibdir}/anapuce/help
%{rlibdir}/anapuce/data
%{rlibdir}/anapuce/R
%{rlibdir}/anapuce/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora