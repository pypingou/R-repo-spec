%global packname  rPorta
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          R/PORTA interface

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An R interface to a modified version of PORTA. For more information on
PORTA see http://www.zib.de/Optimization/Software/Porta/.

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
%doc %{rlibdir}/rPorta/html
%doc %{rlibdir}/rPorta/DESCRIPTION
%{rlibdir}/rPorta/help
%{rlibdir}/rPorta/libs
%{rlibdir}/rPorta/Meta
%{rlibdir}/rPorta/NAMESPACE
%{rlibdir}/rPorta/INDEX
%{rlibdir}/rPorta/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.9-1
- initial package for Fedora