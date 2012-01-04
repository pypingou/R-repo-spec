%global packname  PredictiveRegression
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Prediction Intervals for Three Basic Statistical Models

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Three prediction algorithms described in the paper "On-line predictive
linear regression" (Annals of Statistics, 2008)

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
%doc %{rlibdir}/PredictiveRegression/DESCRIPTION
%doc %{rlibdir}/PredictiveRegression/html
%{rlibdir}/PredictiveRegression/demo
%{rlibdir}/PredictiveRegression/help
%{rlibdir}/PredictiveRegression/INDEX
%{rlibdir}/PredictiveRegression/R
%{rlibdir}/PredictiveRegression/Meta
%{rlibdir}/PredictiveRegression/NAMESPACE
%{rlibdir}/PredictiveRegression/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora