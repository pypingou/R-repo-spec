%global packname  dafs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.36
Release:          1%{?dist}
Summary:          Data analysis for forensic scientists

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-36.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-s20x 

BuildRequires:    R-devel tex(latex) R-s20x 

%description
Data and miscellanea to support the book "Introduction to Data analysis
with R for Forensic Scientists", Curran, J.M. 2010 CRC Press ISBN:

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
%doc %{rlibdir}/dafs/html
%doc %{rlibdir}/dafs/DESCRIPTION
%{rlibdir}/dafs/INDEX
%{rlibdir}/dafs/help
%{rlibdir}/dafs/data
%{rlibdir}/dafs/Meta
%{rlibdir}/dafs/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.36-1
- initial package for Fedora