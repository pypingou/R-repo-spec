%global packname  MFDF
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Modeling Functional Data in Finance

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fda R-zoo 

BuildRequires:    R-devel tex(latex) R-fda R-zoo 

%description
The package contains functions designed to modeling or analyzing the
functional data arising in financial research and practice, as well as
some interesting data sets.

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
%doc %{rlibdir}/MFDF/html
%doc %{rlibdir}/MFDF/DESCRIPTION
%{rlibdir}/MFDF/R
%{rlibdir}/MFDF/NAMESPACE
%{rlibdir}/MFDF/Meta
%{rlibdir}/MFDF/data
%{rlibdir}/MFDF/help
%{rlibdir}/MFDF/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora