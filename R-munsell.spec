%global packname  munsell
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Munsell colour system

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-colorspace 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-colorspace 


%description
Functions for exploring and using the Munsell colour system

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
%doc %{rlibdir}/munsell/DESCRIPTION
%doc %{rlibdir}/munsell/html
%doc %{rlibdir}/munsell/NEWS
%{rlibdir}/munsell/NAMESPACE
%{rlibdir}/munsell/Meta
%{rlibdir}/munsell/help
%{rlibdir}/munsell/R
%{rlibdir}/munsell/raw
%{rlibdir}/munsell/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora