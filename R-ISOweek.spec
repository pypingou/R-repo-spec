%global packname  ISOweek
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Week of the year and weekday according to ISO 8601

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-stringr 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-stringr 


%description
This is an substitute for the %V and %u formats which are not implemented
on Windows. In addition, the package offers functions to convert from
standard calender format yyyy-mm-dd to and from ISO 8601 week format

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2-1
- initial package for Fedora