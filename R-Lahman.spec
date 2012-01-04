%global packname  Lahman
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Sean Lahman's Baseball Database

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides the tables from Sean Lahman's Baseball Database as a
set of R data.frames.  It uses the data on pitching, hitting and fielding
performance and other tables from 1871 through 2010, as recorded in
version 5.8 of the database.

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
%doc %{rlibdir}/Lahman/DESCRIPTION
%doc %{rlibdir}/Lahman/NEWS
%doc %{rlibdir}/Lahman/html
%{rlibdir}/Lahman/INDEX
%{rlibdir}/Lahman/R
%{rlibdir}/Lahman/demo
%{rlibdir}/Lahman/NAMESPACE
%{rlibdir}/Lahman/Meta
%{rlibdir}/Lahman/data
%{rlibdir}/Lahman/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora