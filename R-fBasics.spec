%global packname  fBasics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2110.79
Release:          1%{?dist}
Summary:          Rmetrics - Markets and Basic Statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-methods R-timeDate R-timeSeries 

BuildRequires:    R-devel tex(latex) R-MASS R-methods R-timeDate R-timeSeries 

%description
Environment for teaching "Financial Engineering and Computational Finance"
NOTE: SEVERAL PARTS ARE STILL PRELIMINARY AND MAY BE CHANGED IN THE
FUTURE. THIS TYPICALLY INCLUDES FUNCTION AND ARGUMENT NAMES, AS WELL AS
DEFAULTS FOR ARGUMENTS AND RETURN VALUES. Please donate, www.rmetrics.org,
to support future activities of the Rmetrics association.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2110.79-1
- initial package for Fedora