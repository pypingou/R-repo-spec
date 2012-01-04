%global packname  rbugs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Fusing R and OpenBugs

Group:            Applications/Engineering 
License:          GPL (>= 3.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions to prepare files needed for running BUGS in batch-mode, and
running BUGS from R. Support for Linux and Windows systems with OpenBugs
is emphasized.

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
%doc %{rlibdir}/rbugs/html
%doc %{rlibdir}/rbugs/DESCRIPTION
%{rlibdir}/rbugs/INDEX
%{rlibdir}/rbugs/Meta
%{rlibdir}/rbugs/docs
%{rlibdir}/rbugs/R
%{rlibdir}/rbugs/data
%{rlibdir}/rbugs/OpenBUGS
%{rlibdir}/rbugs/bugs
%{rlibdir}/rbugs/help
%{rlibdir}/rbugs/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.3-1
- initial package for Fedora