%global packname  Devore5
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.5
Release:          1%{?dist}
Summary:          Data sets from Devore's "Prob and Stat for Eng (5th ed)"

Group:            Applications/Engineering 
License:          GPL version 2 or later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data sets and sample analyses from Jay L. Devore (2000), "Probability and
Statistics for Engineering and the Sciences (5th ed)", Duxbury.

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
%doc %{rlibdir}/Devore5/DESCRIPTION
%doc %{rlibdir}/Devore5/html
%{rlibdir}/Devore5/data
%{rlibdir}/Devore5/NAMESPACE
%{rlibdir}/Devore5/INDEX
%{rlibdir}/Devore5/R
%{rlibdir}/Devore5/Meta
%{rlibdir}/Devore5/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.5-1
- initial package for Fedora