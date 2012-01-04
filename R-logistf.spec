%global packname  logistf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.10
Release:          1%{?dist}
Summary:          Firth's bias reduced logistic regression

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Firth's bias reduced logistic regression approach with penalized profile
likelihood based confidence intervals for parameter estimates.

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
%doc %{rlibdir}/logistf/html
%doc %{rlibdir}/logistf/DESCRIPTION
%{rlibdir}/logistf/help
%{rlibdir}/logistf/data
%{rlibdir}/logistf/NAMESPACE
%{rlibdir}/logistf/Meta
%{rlibdir}/logistf/INDEX
%{rlibdir}/logistf/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10-1
- initial package for Fedora