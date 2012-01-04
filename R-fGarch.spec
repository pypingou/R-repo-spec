%global packname  fGarch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2110.80
Release:          1%{?dist}
Summary:          Rmetrics - Autoregressive Conditional Heteroskedastic Modelling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-methods R-timeDate R-timeSeries R-fBasics 


BuildRequires:    R-devel tex(latex) R-stats R-graphics R-methods R-timeDate R-timeSeries R-fBasics



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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2110.80-1
- initial package for Fedora