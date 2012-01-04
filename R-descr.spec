%global packname  descr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Descriptive statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-xtable R-ENmisc 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-xtable R-ENmisc 


%description
This package contains functions to describe weighted categorical variables
and functions to facilitate the character encoding conversion of objects.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.2-1
- initial package for Fedora