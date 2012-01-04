%global packname  Daim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Diagnostic accuracy of classification models.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Several functions for evaluating the accuracy of classification models.
The package provide the following performance measures: "cv", "0.632" and
"0.632+" estimation of the misclassification rate, sensitivity, specifity
and auc. If an application is computationally intensive, parallel
execution can be used to reduce the time taken.

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
%doc %{rlibdir}/Daim/DESCRIPTION
%doc %{rlibdir}/Daim/html
%{rlibdir}/Daim/INDEX
%{rlibdir}/Daim/Meta
%{rlibdir}/Daim/NAMESPACE
%{rlibdir}/Daim/libs
%{rlibdir}/Daim/R
%{rlibdir}/Daim/data
%{rlibdir}/Daim/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora