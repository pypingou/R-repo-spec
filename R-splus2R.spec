%global packname  splus2R
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Supplemental S-PLUS functionality in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Currently there are many functions in S-PLUS that are missing in R. To
facilitate the conversion of S-PLUS packages to R packages, this package
provides some missing S-PLUS functionality in R.

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
%doc %{rlibdir}/splus2R/DESCRIPTION
%doc %{rlibdir}/splus2R/doc
%doc %{rlibdir}/splus2R/html
%{rlibdir}/splus2R/help
%{rlibdir}/splus2R/examples.t
%{rlibdir}/splus2R/Meta
%{rlibdir}/splus2R/INDEX
%{rlibdir}/splus2R/demo
%{rlibdir}/splus2R/R
%{rlibdir}/splus2R/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora