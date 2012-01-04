%global packname  plus
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Penalized Linear Unbiased Selection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grDevices R-graphics R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-grDevices R-graphics R-stats R-utils 

%description
Efficient procedures for fitting an entire regression sequences with
different model types.

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
%doc %{rlibdir}/plus/html
%doc %{rlibdir}/plus/DESCRIPTION
%{rlibdir}/plus/help
%{rlibdir}/plus/data
%{rlibdir}/plus/NAMESPACE
%{rlibdir}/plus/Meta
%{rlibdir}/plus/INDEX
%{rlibdir}/plus/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora