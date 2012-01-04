%global packname  SwissAir
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.01
Release:          1%{?dist}
Summary:          Air Quality Data of Switzerland for one year in 30 min Resolution

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Ozone, NOx (= Sum of Nitrogenmonoxide and Nitrogendioxide),
Nitrogenmonoxide, ambient temperature, dew point, wind speed and wind
direction at 3 sites around lake of Lucerne in Central Switzerland in 30
min time resolution for year 2004.

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
%doc %{rlibdir}/SwissAir/html
%doc %{rlibdir}/SwissAir/DESCRIPTION
%{rlibdir}/SwissAir/Meta
%{rlibdir}/SwissAir/INDEX
%{rlibdir}/SwissAir/NAMESPACE
%{rlibdir}/SwissAir/data
%{rlibdir}/SwissAir/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.01-1
- initial package for Fedora