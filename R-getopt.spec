%global packname  getopt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.17
Release:          1%{?dist}
Summary:          C-like getopt behavior.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Use this with Rscript to write ``#!'' shebang scripts that accept short
and long flags/options.

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
%doc %{rlibdir}/getopt/html
%doc %{rlibdir}/getopt/DESCRIPTION
%{rlibdir}/getopt/INDEX
%{rlibdir}/getopt/Meta
%{rlibdir}/getopt/NAMESPACE
%{rlibdir}/getopt/help
%{rlibdir}/getopt/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.17-1
- initial package for Fedora