%global packname  fRegression
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2100.76
Release:          1%{?dist}
Summary:          Regression Based Decision and Prediction

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-mgcv R-nnet R-polspline R-timeDate R-timeSeries R-fBasics R-fTrading R-fMultivar 


BuildRequires:    R-devel tex(latex) R-methods R-mgcv R-nnet R-polspline R-timeDate R-timeSeries R-fBasics R-fTrading R-fMultivar



%description
Environment for teaching "Financial Engineering and Computational Finance"

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
%changelog
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2100.76-1
- initial package for Fedora