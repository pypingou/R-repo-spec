%global packname  snowFT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Fault Tolerant Simple Network of Workstations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-snow 

BuildRequires:    R-devel tex(latex) R-snow 

%description
Extension of the snow package supporting fault tolerant and reproducible
applications, as well as supporting easy-to-use parallel programming -
only one function is needed.

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
%doc %{rlibdir}/snowFT/html
%doc %{rlibdir}/snowFT/DESCRIPTION
%{rlibdir}/snowFT/help
%{rlibdir}/snowFT/R
%{rlibdir}/snowFT/INDEX
%{rlibdir}/snowFT/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora