%global packname  cumSeg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Change point detection in genomic sequences

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lars 

BuildRequires:    R-devel tex(latex) R-lars 

%description
Estimation of number and location of change points in mean-shift
(piecewise constant) models. Particularly useful to model genomic
sequences of continuous measurements.

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
%doc %{rlibdir}/cumSeg/DESCRIPTION
%doc %{rlibdir}/cumSeg/html
%{rlibdir}/cumSeg/help
%{rlibdir}/cumSeg/data
%{rlibdir}/cumSeg/R
%{rlibdir}/cumSeg/INDEX
%{rlibdir}/cumSeg/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora