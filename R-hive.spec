%global packname  hive
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.13
Release:          1%{?dist}
Summary:          Hadoop InteractiVE

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-rJava R-tools R-XML 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-rJava R-tools R-XML 


%description
Hadoop InteractiVE, is an R extension facilitating distributed computing
via the MapReduce paradigm. It provides an easy to use interface to
Hadoop, the Hadoop Distributed File System (HDFS), and Hadoop Streaming.

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
%doc %{rlibdir}/hive/DESCRIPTION
%doc %{rlibdir}/hive/html
%{rlibdir}/hive/NAMESPACE
%{rlibdir}/hive/Meta
%{rlibdir}/hive/defaults
%{rlibdir}/hive/R
%{rlibdir}/hive/help
%{rlibdir}/hive/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.13-1
- initial package for Fedora