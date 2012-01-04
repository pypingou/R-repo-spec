%global packname  openintro
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          OpenIntro data sets and supplement functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package is a supplement to the OpenIntro open source book project.
The package contains data sets used in the book along with plotting
functions to reproduce the book's figures. Note that many functions and
examples include color transparency, which may result in partially some
plotting elements not showing up properly in Windows (see Details section
of the openintro package help file for details).

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
%doc %{rlibdir}/openintro/html
%doc %{rlibdir}/openintro/DESCRIPTION
%{rlibdir}/openintro/data
%{rlibdir}/openintro/NAMESPACE
%{rlibdir}/openintro/R
%{rlibdir}/openintro/INDEX
%{rlibdir}/openintro/Meta
%{rlibdir}/openintro/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora