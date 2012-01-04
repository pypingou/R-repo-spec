%global packname  TSAgg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Time series Aggregation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Time series aggregation for incomplete time series data.

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
%doc %{rlibdir}/TSAgg/html
%doc %{rlibdir}/TSAgg/DESCRIPTION
%{rlibdir}/TSAgg/Meta
%{rlibdir}/TSAgg/INDEX
%{rlibdir}/TSAgg/data
%{rlibdir}/TSAgg/NAMESPACE
%{rlibdir}/TSAgg/R
%{rlibdir}/TSAgg/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora