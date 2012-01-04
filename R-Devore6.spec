%global packname  Devore6
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.6
Release:          1%{?dist}
Summary:          Data sets from Devore's "Prob and Stat for Eng (6th ed)"

Group:            Applications/Engineering 
License:          GPL version 2 or later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Data sets and sample analyses from Jay L. Devore (2003), "Probability and
Statistics for Engineering and the Sciences (6th ed)", Duxbury.

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
%doc %{rlibdir}/Devore6/html
%doc %{rlibdir}/Devore6/doc
%doc %{rlibdir}/Devore6/DESCRIPTION
%{rlibdir}/Devore6/NAMESPACE
%{rlibdir}/Devore6/Meta
%{rlibdir}/Devore6/data
%{rlibdir}/Devore6/INDEX
RPM build errors:
%{rlibdir}/Devore6/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- initial package for Fedora