%global packname  inference
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Functions to extract inferential values of a fitted model object

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sandwich R-methods 

BuildRequires:    R-devel tex(latex) R-sandwich R-methods 

%description
Collection of functions to extract inferential values (point estimates,
confidence intervals, p-values, etc) of a fitted model object into a
matrix-like object that can be used for table/report generation; transform
point estimates via the delta method.

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
%doc %{rlibdir}/inference/DESCRIPTION
%doc %{rlibdir}/inference/html
%{rlibdir}/inference/help
%{rlibdir}/inference/NAMESPACE
%{rlibdir}/inference/R
%{rlibdir}/inference/INDEX
%{rlibdir}/inference/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora