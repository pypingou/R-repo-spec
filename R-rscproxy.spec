%global packname  rscproxy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          statconn: provides portable C-style interface to R (StatConnector)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
rscproxy library provides an interface to R used by third party
applications, most notable, but not limited to, statconnDCOM, ROOo and
other systems.

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
%doc %{rlibdir}/rscproxy/DESCRIPTION
%doc %{rlibdir}/rscproxy/html
%{rlibdir}/rscproxy/NAMESPACE
%{rlibdir}/rscproxy/libs
%{rlibdir}/rscproxy/include
%{rlibdir}/rscproxy/Meta
%{rlibdir}/rscproxy/INDEX
%{rlibdir}/rscproxy/R
%{rlibdir}/rscproxy/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora