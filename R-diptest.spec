%global packname  diptest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.75.1
Release:          1%{?dist}
Summary:          Hartigan's dip test statistic for unimodality - corrected code

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.75-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Compute Hartigan's dip test statistic for unimodality

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
%doc %{rlibdir}/diptest/html
%doc %{rlibdir}/diptest/doc
%doc %{rlibdir}/diptest/DESCRIPTION
%{rlibdir}/diptest/R
%{rlibdir}/diptest/help
%{rlibdir}/diptest/INDEX
%{rlibdir}/diptest/NAMESPACE
%{rlibdir}/diptest/extraData
%{rlibdir}/diptest/libs
%{rlibdir}/diptest/data
%{rlibdir}/diptest/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.75.1-1
- initial package for Fedora