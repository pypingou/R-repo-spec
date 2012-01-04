%global packname  wombsoft
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Wombling Computation

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Analyses individually geo-referenced multilocus genotypes for the
inferences of genetic boundaries between populations. It is based on the
wombling method that estimates the systemic function by looking for the
local variation of the allele frequencies. The systemic function
estimation is based on the local polynomial regression, and a binomial
test assess the significance of boundaries. The method applies to
codominant or dominant markers and allows for missing data.

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
%doc %{rlibdir}/wombsoft/html
%doc %{rlibdir}/wombsoft/DESCRIPTION
%{rlibdir}/wombsoft/INDEX
%{rlibdir}/wombsoft/Meta
%{rlibdir}/wombsoft/help
%{rlibdir}/wombsoft/R
RPM build errors:
%{rlibdir}/wombsoft/libs
%{rlibdir}/wombsoft/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora