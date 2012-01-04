%global packname  popbio
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Construction and analysis of matrix population models

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Construct and analyze projection matrix models from a demography study of
marked individuals classified by age or stage. The package covers methods
described in Matrix Population Models by Caswell (2001) and Quantitative
Conservation Biology by Morris and Doak (2002).

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
%doc %{rlibdir}/popbio/doc
%doc %{rlibdir}/popbio/CITATION
%doc %{rlibdir}/popbio/DESCRIPTION
%doc %{rlibdir}/popbio/html
%{rlibdir}/popbio/data
%{rlibdir}/popbio/R
%{rlibdir}/popbio/INDEX
%{rlibdir}/popbio/ChangeLog
%{rlibdir}/popbio/help
%{rlibdir}/popbio/demo
%{rlibdir}/popbio/NAMESPACE
%{rlibdir}/popbio/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.1-1
- initial package for Fedora