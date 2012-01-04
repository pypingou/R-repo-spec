%global packname  PhysicalActivity
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Process Physical Activity Accelerometer Data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains functions to classify monitor wear and nonwear time
intervals in accelerometer data collected to assess physical activity in
free-living condition. The package also contains functions to make plot
for accelerometer data, and to obtain the summary of daily monitor wear
time and the mean of monitor wear time during valid days. A monitored day
is considered valid if the total minutes of classified monitor wear time
per day is greater than a user defined cutoff.

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
%doc %{rlibdir}/PhysicalActivity/html
%doc %{rlibdir}/PhysicalActivity/DESCRIPTION
%{rlibdir}/PhysicalActivity/R
%{rlibdir}/PhysicalActivity/help
%{rlibdir}/PhysicalActivity/Meta
%{rlibdir}/PhysicalActivity/NAMESPACE
%{rlibdir}/PhysicalActivity/data
%{rlibdir}/PhysicalActivity/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora