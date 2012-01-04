%global packname  pwt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          7.0.0
Release:          1%{?dist}
Summary:          Penn World Table

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_7.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The Penn World Table provides purchasing power parity and national income
accounts converted to international prices for 189 countries for some or
all of the years 1950-2009.

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
%doc %{rlibdir}/pwt/NEWS
%doc %{rlibdir}/pwt/html
%doc %{rlibdir}/pwt/DESCRIPTION
%doc %{rlibdir}/pwt/CITATION
%{rlibdir}/pwt/Meta
%{rlibdir}/pwt/NAMESPACE
%{rlibdir}/pwt/INDEX
%{rlibdir}/pwt/help
%{rlibdir}/pwt/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 7.0.0-1
- initial package for Fedora