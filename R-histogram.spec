%global packname  histogram
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.23
Release:          1%{?dist}
Summary:          Construction of regular and irregular histograms with different options for automatic choice of bins

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-23.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Automatic construction of regular and irregular histograms as described in
Rozenholc/Mildenberger/Gather (2009).

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
%doc %{rlibdir}/histogram/html
%doc %{rlibdir}/histogram/DESCRIPTION
%{rlibdir}/histogram/NAMESPACE
%{rlibdir}/histogram/R
%{rlibdir}/histogram/help
%{rlibdir}/histogram/INDEX
%{rlibdir}/histogram/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.23-1
- initial package for Fedora