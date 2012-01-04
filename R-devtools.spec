%global packname  devtools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Tools to make developing R code easier

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-RCurl R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-RCurl R-utils 


%description
Collection of package development tools

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora