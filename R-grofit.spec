%global packname  grofit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          The package was developed to fit fit many growth curves obtained under different conditions.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package was developd to fit fit many growth curves obtained under
different conditions in order to derive a conclusive dose-repsonse curve,
for instance for a compound that potentially affects growth. grofit fits
data to different parametric models (function gcFitModel) and in addition
provides a model free spline fit (function gcFitSpline) to circumvent
systematic errors that might occur within application of parametric

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
%doc %{rlibdir}/grofit/CITATION
%doc %{rlibdir}/grofit/doc
%doc %{rlibdir}/grofit/html
%doc %{rlibdir}/grofit/DESCRIPTION
%{rlibdir}/grofit/INDEX
%{rlibdir}/grofit/NAMESPACE
%{rlibdir}/grofit/Meta
%{rlibdir}/grofit/data
%{rlibdir}/grofit/R
%{rlibdir}/grofit/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora