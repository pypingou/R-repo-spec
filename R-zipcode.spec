%global packname  zipcode
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          U.S. ZIP Code database

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains the "CivicSpace US ZIP Code Database" by Schuyler
Erle, August 2004 as a data.frame. Believed to contain over 98% of U.S.
ZIP Codes as of 2004 The source data is available in CSV from
\url{http://www.boutell.com/zipcodes/} and
\url{http://mappinghacks.com/data/} and has been released under the
Creative Commons Share-Alike license.

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
%doc %{rlibdir}/zipcode/DESCRIPTION
%doc %{rlibdir}/zipcode/NEWS
%doc %{rlibdir}/zipcode/html
%{rlibdir}/zipcode/NAMESPACE
%{rlibdir}/zipcode/Meta
%{rlibdir}/zipcode/R
%{rlibdir}/zipcode/help
%{rlibdir}/zipcode/INDEX
%{rlibdir}/zipcode/LICENSE
%{rlibdir}/zipcode/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora