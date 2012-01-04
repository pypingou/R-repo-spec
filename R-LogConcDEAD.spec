%global packname  LogConcDEAD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.4
Release:          1%{?dist}
Summary:          Log-concave Density Estimation in Arbitrary Dimensions

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-MASS R-mvtnorm 

%description
Computes a log-concave (maximum likelihood) estimator for i.i.d. data in
any number of dimensions.

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
%doc %{rlibdir}/LogConcDEAD/html
%doc %{rlibdir}/LogConcDEAD/doc
%doc %{rlibdir}/LogConcDEAD/DESCRIPTION
%doc %{rlibdir}/LogConcDEAD/CITATION
%{rlibdir}/LogConcDEAD/R
%{rlibdir}/LogConcDEAD/help
%{rlibdir}/LogConcDEAD/INDEX
%{rlibdir}/LogConcDEAD/libs
%{rlibdir}/LogConcDEAD/Meta
%{rlibdir}/LogConcDEAD/LICENSE
%{rlibdir}/LogConcDEAD/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.4-1
- initial package for Fedora