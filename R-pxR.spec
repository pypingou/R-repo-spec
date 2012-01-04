%global packname  pxR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.24
Release:          1%{?dist}
Summary:          PC-Axis with R

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The pxR package provides a set of functions for reading and writing
PC-Axis files, used by different statistical organizations around the
globe for data disemination.

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
%doc %{rlibdir}/pxR/DESCRIPTION
%doc %{rlibdir}/pxR/html
%{rlibdir}/pxR/NAMESPACE
%{rlibdir}/pxR/Meta
%{rlibdir}/pxR/extdata
%{rlibdir}/pxR/R
%{rlibdir}/pxR/help
%{rlibdir}/pxR/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.24-1
- initial package for Fedora