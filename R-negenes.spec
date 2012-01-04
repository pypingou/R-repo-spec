%global packname  negenes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.98.9
Release:          1%{?dist}
Summary:          Estimating the number of essential genes in a genome

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.98-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Estimating the number of essential genes in a genome on the basis of data
from a random transposon mutagenesis experiment, through the use of a
Gibbs sampler.

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
%doc %{rlibdir}/negenes/html
%doc %{rlibdir}/negenes/CITATION
%doc %{rlibdir}/negenes/DESCRIPTION
%{rlibdir}/negenes/NAMESPACE
%{rlibdir}/negenes/Meta
%{rlibdir}/negenes/STATUS.txt
%{rlibdir}/negenes/libs
%{rlibdir}/negenes/INDEX
RPM build errors:
%{rlibdir}/negenes/README.txt
%{rlibdir}/negenes/help
%{rlibdir}/negenes/data
%{rlibdir}/negenes/R
%{rlibdir}/negenes/LICENSE.txt

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.98.9-1
- initial package for Fedora