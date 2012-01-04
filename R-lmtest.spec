%global packname  lmtest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.29
Release:          1%{?dist}
Summary:          Testing Linear Regression Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-29.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-zoo 

BuildRequires:    R-devel tex(latex) R-stats R-zoo 

%description
A collection of tests, data sets, and examples for diagnostic checking in
linear regression models. Furthermore, some generic tools for inference in
parametric models are provided.

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
%doc %{rlibdir}/lmtest/NEWS
%doc %{rlibdir}/lmtest/CITATION
%doc %{rlibdir}/lmtest/html
%doc %{rlibdir}/lmtest/doc
%doc %{rlibdir}/lmtest/DESCRIPTION
%{rlibdir}/lmtest/INDEX
%{rlibdir}/lmtest/Meta
%{rlibdir}/lmtest/help
%{rlibdir}/lmtest/NAMESPACE
%{rlibdir}/lmtest/R
%{rlibdir}/lmtest/libs
%{rlibdir}/lmtest/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.29-1
- initial package for Fedora