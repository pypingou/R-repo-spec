%global packname  tframePlus
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.2
Release:          1%{?dist}
Summary:          Time Frame coding kernel extensions

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tframe 
Requires:         R-tframe R-methods R-timeSeries 

BuildRequires:    R-devel tex(latex) R-tframe
BuildRequires:    R-tframe R-methods R-timeSeries 


%description
Extensions and additional tframe utilities.

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
%doc %{rlibdir}/tframePlus/doc
%doc %{rlibdir}/tframePlus/html
%doc %{rlibdir}/tframePlus/DESCRIPTION
%doc %{rlibdir}/tframePlus/NEWS
%{rlibdir}/tframePlus/LICENSE
%{rlibdir}/tframePlus/INDEX
%{rlibdir}/tframePlus/help
%{rlibdir}/tframePlus/Meta
%{rlibdir}/tframePlus/R
%{rlibdir}/tframePlus/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.2-1
- initial package for Fedora