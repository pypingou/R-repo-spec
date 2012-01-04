%global packname  smoothmest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Smoothed M-estimators for 1-dimensional location

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Some M-estimators for 1-dimensional location (Bisquare, ML for the Cauchy
distribution, and the estimators from application of the smoothing
principle introduced in Hampel, Hennig and Ronchetti (2011) to the above,
the Huber M-estimator, and the median, main function is smoothm), and
Pitman estimator.

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
%doc %{rlibdir}/smoothmest/DESCRIPTION
%doc %{rlibdir}/smoothmest/html
%{rlibdir}/smoothmest/Meta
%{rlibdir}/smoothmest/R
%{rlibdir}/smoothmest/INDEX
%{rlibdir}/smoothmest/NAMESPACE
%{rlibdir}/smoothmest/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora