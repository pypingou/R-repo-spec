%global packname  matlab
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.9
Release:          1%{?dist}
Summary:          MATLAB emulation package

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Emulate MATLAB code using R

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
%doc %{rlibdir}/matlab/DESCRIPTION
%doc %{rlibdir}/matlab/html
%doc %{rlibdir}/matlab/NEWS
%{rlibdir}/matlab/R
%{rlibdir}/matlab/NAMESPACE
%{rlibdir}/matlab/help
%{rlibdir}/matlab/Meta
%{rlibdir}/matlab/INDEX
%{rlibdir}/matlab/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.9-1
- initial package for Fedora