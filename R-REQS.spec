%global packname  REQS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.12
Release:          1%{?dist}
Summary:          R/EQS Interface

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gtools 

BuildRequires:    R-devel tex(latex) R-gtools 

%description
This package contains the function run.eqs() which calls an EQS script
file, executes the EQS estimation, and, finally, imports the results as R
objects. These two steps can be performed separately: call.eqs() calls and
executes EQS, whereas read.eqs() imports existing EQS outputs as objects
into R. It requires EQS 6.2 (build 98 or higher).

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
%doc %{rlibdir}/REQS/DESCRIPTION
%doc %{rlibdir}/REQS/html
%{rlibdir}/REQS/INDEX
%{rlibdir}/REQS/R
%{rlibdir}/REQS/help
%{rlibdir}/REQS/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.12-1
- initial package for Fedora