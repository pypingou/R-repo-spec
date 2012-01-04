%global packname  hypergeo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          The hypergeometric function

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-contfrac R-elliptic 

BuildRequires:    R-devel tex(latex) R-contfrac R-elliptic 

%description
The hypergeometric function, hypergeo(), for complex numbers

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
%doc %{rlibdir}/hypergeo/html
%doc %{rlibdir}/hypergeo/DESCRIPTION
%doc %{rlibdir}/hypergeo/CITATION
%{rlibdir}/hypergeo/INDEX
%{rlibdir}/hypergeo/R
%{rlibdir}/hypergeo/NAMESPACE
%{rlibdir}/hypergeo/help
%{rlibdir}/hypergeo/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora