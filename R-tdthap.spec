%global packname  tdthap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          TDT tests for extended haplotypes

Group:            Applications/Engineering 
License:          Artistic License
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Clayton, D. and Jones, H.B. (1999), Transmission/disequilibrium tests for
extended marker haplotypes, Am. J. Hum. Gen., 65:1161-1169.

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
%doc %{rlibdir}/tdthap/DESCRIPTION
%doc %{rlibdir}/tdthap/html
%{rlibdir}/tdthap/help
%{rlibdir}/tdthap/R
%{rlibdir}/tdthap/INDEX
%{rlibdir}/tdthap/NAMESPACE
%{rlibdir}/tdthap/libs
%{rlibdir}/tdthap/test.ped
%{rlibdir}/tdthap/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora