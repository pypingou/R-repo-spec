%global packname  GGally
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Extension to ggplot2.

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ggplot2 R-stringr 

BuildRequires:    R-devel tex(latex) R-ggplot2 R-stringr 

%description
Package contains templates for different plots to be combined into a plot
matrix, as well as a parallel coordinate plot function.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora