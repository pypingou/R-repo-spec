%global packname  SNPmaxsel
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Maximally selected statistics for SNP data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-combinat 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-combinat 

%description
This package implements asymptotic methods related to maximally selected
statistics, with applications to SNP data.

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
%doc %{rlibdir}/SNPmaxsel/html
%doc %{rlibdir}/SNPmaxsel/DESCRIPTION
%{rlibdir}/SNPmaxsel/Meta
%{rlibdir}/SNPmaxsel/help
%{rlibdir}/SNPmaxsel/INDEX
%{rlibdir}/SNPmaxsel/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora