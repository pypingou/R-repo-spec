%global packname  NADA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.3
Release:          1%{?dist}
Summary:          Nondetects And Data Analysis for environmental data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-survival 

BuildRequires:    R-devel tex(latex) R-methods R-survival 

%description
Contains methods described by Dennis R. Helsel in his book "Nondetects And
Data Analysis: Statistics for Censored Environmental Data"

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
%doc %{rlibdir}/NADA/html
%doc %{rlibdir}/NADA/DESCRIPTION
%{rlibdir}/NADA/Meta
%{rlibdir}/NADA/data
%{rlibdir}/NADA/R
%{rlibdir}/NADA/NAMESPACE
%{rlibdir}/NADA/help
%{rlibdir}/NADA/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.3-1
- initial package for Fedora