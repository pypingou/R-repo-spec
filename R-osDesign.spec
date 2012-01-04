%global packname  osDesign
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Design and analysis of observational studies

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The osDesign serves for planning an observational study. Currently,
functionality is focused on the two-phase and case-control designs.
Functions in this packages provides Monte Carlo based evaluation of
operating characteristics such as powers for estimators of the components
of a logistic regression model.

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
%doc %{rlibdir}/osDesign/CITATION
%doc %{rlibdir}/osDesign/DESCRIPTION
%doc %{rlibdir}/osDesign/html
%{rlibdir}/osDesign/NAMESPACE
%{rlibdir}/osDesign/data
%{rlibdir}/osDesign/INDEX
%{rlibdir}/osDesign/R
%{rlibdir}/osDesign/help
%{rlibdir}/osDesign/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora