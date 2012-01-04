%global packname  corrgram
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Plot a correlogram

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-seriation R-stats 

BuildRequires:    R-devel tex(latex) R-graphics R-seriation R-stats 

%description
Calculates correlation of variables and displays the results graphically.

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
%doc %{rlibdir}/corrgram/NEWS
%doc %{rlibdir}/corrgram/html
%doc %{rlibdir}/corrgram/DESCRIPTION
%{rlibdir}/corrgram/INDEX
%{rlibdir}/corrgram/data
%{rlibdir}/corrgram/NAMESPACE
%{rlibdir}/corrgram/help
%{rlibdir}/corrgram/R
%{rlibdir}/corrgram/Meta

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora